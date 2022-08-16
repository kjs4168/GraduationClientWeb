import { ActivatedType } from "types/common/activatedType";
import { LicenseType } from "types/common/licenseType";

export interface ReadLicenseResponse {
  sensors: Array<any>;
  allow_features: Array<any>;
  lidar_count: number;
  gpu_algo_node_count: number;
  algo_node_count: number;
  max_argos_session_count: number;
  name: string;
  machine_id: string;
  multiple: number;
  activated: ActivatedType;
  license_type: LicenseType;
  user: string;
  iat: string;
  sub: string;
  nbf: string;
  exp: string;
  created_at: string;
  license_str: string;
}
